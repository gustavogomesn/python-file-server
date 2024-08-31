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

// folders_links = document.querySelectorAll('.folders')
// folders_links.forEach(folder => {
//     folder.addEventListener("dclick",function(e) {
//         e.preventDefault();
//         console.log(e.target)
//         var body = document.querySelector('body')
//         var form = document.createElement("form")
//         var path = document.createElement('input')
//         form.appendChild(path)
//         body.appendChild(form)
//         path.value = this.href
//         form.action= "{{url_for('files')}}"
//         form.method="POST"
//         // form.submit()
//     });
// })


 