function extractFeatures() {
    var form = document.getElementById('extractFeaturesForm');
    form.submit();
}

function submitInput() {
    const fileInput = document.getElementById('fileInput');
    const fileName = document.getElementById('fileName');

    sessionStorage.setItem('selectedFileName', fileInput.files[0].name);
    fileName.textContent = sessionStorage.getItem('selectedFileName');
    document.getElementById('uploadForm').submit();
}


if (sessionStorage.getItem('selectedFileName')) {
    document.getElementById('fileName').textContent = sessionStorage.getItem('selectedFileName');
    document.getElementById('img_div').style.maxWidth = '1000px';
}


function searchColorOrTexture() {
    if(document.getElementById("ColorTextureToggle").checked){
        location.href='/image_texture_search';
    }
    else{
        location.href='/image_color_search';
    }
}