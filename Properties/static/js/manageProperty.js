const radioButtons = document.getElementsByName('option');
const rentInputContainer = document.getElementById('forRent');
const sellInputContainer = document.getElementById('forSell');
const selectedOption = document.getElementById('optionSelected');

radioButtons.forEach((radio) => {
    rentInputContainer.style.display = 'none';
    sellInputContainer.style.display = 'none';
    radio.addEventListener('change', () => {
        if (radio.value === 'ForRent') {
            rentInputContainer.style.display = 'block';
            sellInputContainer.style.display = 'none';
            selectedOption.textContent = 'This Property is for Rent'
        } 
        else if (radio.value === 'ForSale') {
            rentInputContainer.style.display = 'none';
            sellInputContainer.style.display = 'block';
            selectedOption.textContent = 'This Property is for Sale'
        }
    });
});