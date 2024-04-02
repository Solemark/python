const submit_data = () => {
    let height = document.getElementById("height").value
    let weight = document.getElementById("weight").value
    //const res = await fetch(`/${height}/${weight}`).json()
    clear_data()
    document.getElementById("output").innerHTML = `H: ${height}\t W: ${weight}`
}

const clear_data = () => {
    document.getElementById("height").value = ""
    document.getElementById("weight").value = ""
    document.getElementById("output").innerHTML = ""
}
