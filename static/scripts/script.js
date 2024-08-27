const deleteFolderButtons = document.querySelectorAll('.delete-folder-button')

function handleDeleteButton(e){
    response = confirm('Are you sure you want to delete it?\nThere may be important files inside this folder')
    if (!response){
        e.preventDefault()
    }
}

deleteFolderButtons.forEach(button => {
    button.addEventListener('click', e => {
        handleDeleteButton(e)
    })
})
