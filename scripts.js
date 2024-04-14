document.getElementById('image-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const imageFile = document.getElementById('image-input').files[0];

    const formData = new FormData();
    formData.append('image', imageFile);

    const response = await fetch('/', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2>Deceptive/Manipulative Content:</h2>
        <p>${data.is_tampered? 'Yes' : 'No'}</p>
        <h2>Reason:</h2>
        <p>${data.reason}</p>
        <h2>Percentage Confidence:</h2>
        <p>${data.confidence}%</p>
        <h2>Tips:</h2>
        <p>${data.tips}</p>
        ${data.tampered_image? `<img src="${data.tampered_image}" alt="Tampered Image">` : ''}
    `;
});