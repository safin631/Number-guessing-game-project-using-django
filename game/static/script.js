function submitGuess() {
    const guess = document.getElementById('guess').value;
    fetch(`/guess/?guess=${guess}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.message;
        });
}