
let currentDeleteId = null;

function openDeletePopup(fileId, fileName){

currentDeleteId = fileId;

document.getElementById('popupOverlay').style.display = 'flex';

document.getElementById('popupText').innerText =
`Are you sure you want to delete ${fileName}?`;
}

function closeDeletePopup(){

document.getElementById('popupOverlay').style.display = 'none';

currentDeleteId = null;
}

document.getElementById('confirmDeleteBtn').addEventListener('click', async () => {

if(currentDeleteId === null){
return;
}

const response = await fetch(`/delete/${currentDeleteId}`, {
method:'POST'
});

const data = await response.json();

if(data.status === 'deleted'){
location.reload();
}

});
