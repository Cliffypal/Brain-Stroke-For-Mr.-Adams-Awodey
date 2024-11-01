document.getElementById('patient-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const hypertension = document.getElementById('hypertension').value;
    const heartDisease = document.getElementById('heart_disease').value;
    const everMarried = document.getElementById('ever_married').value;
    const workType = document.getElementById('work_type').value;
    const residenceType = document.getElementById('residence_type').value;
    const avgGlucoseLevel = document.getElementById('avg_glucose_level').value;
    const bmi = document.getElementById('bmi').value;
    const smokingStatus = document.getElementById('smoking_status').value;

    // Output result
    const output = `
        Gender: ${gender}<br>
        Age: ${age}<br>
        Hypertension: ${hypertension}<br>
        Heart Disease: ${heartDisease}<br>
        Ever Married: ${everMarried}<br>
        Work Type: ${workType}<br>
        Residence Type: ${residenceType}<br>
        Average Glucose Level: ${avgGlucoseLevel}<br>
        BMI: ${bmi}<br>
        Smoking Status: ${smokingStatus}
    `;

    document.getElementById('output').innerHTML = output;
});
