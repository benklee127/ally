const dragArea = document.querySelector('.drag-area');

dragArea.addEventListener('dragover', (event) => {
        event.preventDefault()
        console.log("drag attempt")
    })

dragArea.addEventListener('dragleave', () => {
    console.log("drag remove")
})

dragArea.addEventListener('drop', (event) => {
    event.preventDefault()
    console.log("drag drop")
})
