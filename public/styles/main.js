let fileData = null;

const postData = async (url = "", data = {}) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

let imageFilesMap = {}
window.onload = () => {

    imageFilesMap = {}

    let fileInputs = document.getElementsByClassName("file-inputs")
    for (let i = 0; i < fileInputs.length; ++i) {
        fileInputs[i].addEventListener("change", (event) => {
            const selectedFile = event.target.files;
            if (selectedFile.length <= 0) return;

            const [imageFile] = selectedFile;
            const fileReader = new FileReader();
            fileReader.onload = () => {
                const srcData = fileReader.result
                imageFilesMap[fileInputs[i].id] = srcData

                // console.log('base64:', srcData)
            };
            fileReader.readAsDataURL(imageFile)
        });
    }
}

async function getFilter(filterName, inp1, imgInp1, imgOut1, inp2 = null, imgInp2 = null) {
    if (inp1 == null || filterName == null) return;

    let img1Base64 = imageFilesMap[inp1]

    document.getElementById(imgInp1).src = img1Base64

    let img1 = img1Base64.split("base64,")[1]

    // console.log(img1);

    let img2Base64 = imageFilesMap[inp2]
    let img2 = null
    if (imgInp2 != null) {
        document.getElementById(imgInp2).src = img2Base64
        img2 = img2Base64.split("base64,")[1]
    }

    let data = {
        "imageFile1": img1,
        "imageFile2": img2,
        "filter": filterName
    }
    // console.log(data);

    let res = await postData("/filter", data)
    // console.log(res);

    let imageOutData = res["img"].slice(2, res["img"].length - 1)

    document.getElementById(imgOut1).src = `data:image/png;base64,${imageOutData}`
}