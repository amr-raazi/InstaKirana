if(["", null, " "].indexOf(localStorage.getItem("location")) +1) {
    localStorage.setItem('location', ("Moradabad"));
}
document.getElementById("delivering").innerHTML = "Delivering in 20 minutes or less to <u>" + localStorage.getItem('location') + "</u>";

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


$(document).ready(function () {
    $('.location-drop-down').change(async function () {
        let selected_value = ($(this).find("option:selected").attr('value'));
        localStorage.setItem('location', (selected_value));
        document.getElementById("delivering").innerHTML = "Delivering in 20 minutes or less to <u>" + localStorage.getItem('location') + "</u>";
        await sleep(800);
        $('.location-drop-down').val("");
    })
})


