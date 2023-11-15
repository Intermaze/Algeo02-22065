function extractFeatures() {
    var form = document.getElementById('extractFeaturesForm');
    form.submit();
}

function submitForm() {
    const fileInput = document.getElementById('fileInput');
    const fileName = document.getElementById('fileName');

    sessionStorage.setItem('selectedFileName', fileInput.files[0].name);
    fileName.textContent = sessionStorage.getItem('selectedFileName');
    document.getElementById('uploadForm').submit();
}

window.onload = function() {
    if (sessionStorage.getItem('selectedFileName')) {
        document.getElementById('fileName').textContent = sessionStorage.getItem('selectedFileName');
    }
};

function searchColorOrTexture() {
    if(document.getElementById("ColorTextureToggle").checked){
        location.href='/image_texture_search';
    }
    else{
        location.href='/image_color_search';
    }
}