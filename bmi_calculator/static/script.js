/**
 * @typedef Rating
 * @type {object}
 * @property {string} rating - BMI rating
 */

const submit_data = () => {
    let height = document.getElementById("height").value
    let weight = document.getElementById("weight").value
    get_rating(height, weight)
}

/**
 * @param {string} height 
 * @param {string} weight 
 */
const get_rating = (height, weight) => {
    fetch(`/data/${height}/${weight}`)
        .then(async (res) => {
            res = await res.json()
            set_output(res)
        })
        .catch((err) => {
            console.log(err)
        })
}

/**
 * @param {Rating} res 
 */
const set_output = (res) => {
    clear_data()
    document.getElementById("output").innerHTML = res.rating
}

const clear_data = () => {
    document.getElementById("height").value = ""
    document.getElementById("weight").value = ""
    document.getElementById("output").innerHTML = ""
}
