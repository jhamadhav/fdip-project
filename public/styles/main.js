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
window.onload = async () => {

    await new Promise(function (resolve, reject) {
        makeFilterDivContent()
        resolve(10);
    })

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

const makeFilterDivContent = () => {
    let divs = document.getElementsByClassName("filter-div")
    for (let i = 0; i < divs.length; ++i) {
        let id = divs[i].id
        let imageCount = divs[i].getAttribute("imgs")
        // console.log(id);
        // console.log(imageCount);

        if (imageCount == "2") {
            divs[i].innerHTML = `
            <h2 class="text-center">Upload image for demo</h2>

            <!-- change ID as per your filter -->
            <input type="file" name="imageFile" id="${id}-filter-inp" class="file-inputs" autocomplete="off">

            <input type="file" name="imageFile" id="${id}-filter-inp-2" class="file-inputs" autocomplete="off">

            <br><br>

            <!-- change the image ID as per your filter -->
            <span>Original Image:</span>
            <br>


            <img src="" id="${id}-filter-img-inp" alt="image-1-input-here">
            <br>
            <img src="" id="${id}-filter-img-inp-2" alt="image-2-input-here">

            <br><br>
            <span>Filter Image:</span>

            <br>
            <img src="" id="${id}-filter-img-out" alt="image-output-here">

            <!-- change the btn id as per your filter name -->
            <button id="${id}-filter-btn"
                onclick='getFilter("${id}","${id}-filter-inp","${id}-filter-img-inp","${id}-filter-img-out","${id}-filter-inp-2","${id}-filter-img-inp-2" )'>Send</button>
            </p>`
            continue
        }

        divs[i].innerHTML = `
            <h2 class="text-center">Upload image for demo</h2>

            <!-- change ID as per your filter -->
            <input type="file" name="imageFile" id="${id}-filter-inp" class="file-inputs" autocomplete="off">

            <br><br>

            <!-- change the image ID as per your filter -->
            <span>Original Image:</span>
            <br>


            <img src="" id="${id}-filter-img-inp" alt="image-input-here">

            <br><br>
            <span>Filter Image:</span>

            <br>
            <img src="" id="${id}-filter-img-out" alt="image-output-here">

            <!-- change the btn id as per your filter name -->
            <button id="${id}-filter-btn"
                onclick='getFilter("${id}","${id}-filter-inp","${id}-filter-img-inp","${id}-filter-img-out" )'>Send</button>
            </p>
        `
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
    if (inp2 != null) {
        document.getElementById(imgInp2).src = img2Base64
        img2 = img2Base64.split("base64,")[1]
    }

    let data = {
        "imageFile1": img1,
        "imageFile2": img2,
        "filter": filterName,
        "imageCount": ((inp2 == null) ? 1 : 2)
    }
    // console.log(data);

    let res = await postData("/filter", data)
    // console.log(res);

    let imageOutData = res["img"].slice(2, res["img"].length - 1)

    document.getElementById(imgOut1).src = `data:image/png;base64,${imageOutData}`
}