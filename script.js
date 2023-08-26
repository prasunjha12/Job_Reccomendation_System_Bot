const chatForm = document.getElementById("chatForm");
const userSkillsInput = document.getElementById("formData");
const responseContainer = document.getElementById("responseContainer");

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append("user_skills", userSkillsInput.value);

    const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: formData
    });

    if (response.ok) {
        const responseData = await response.json();
        const botResponse = responseData.response;

        

        responseContainer.innerHTML = `
            <p><strong>Your Input:</strong> ${userSkillsInput.value}</p>
            <p><strong>Bot Response:</strong> ${botResponse}</p>
        `;
    } else {
        responseContainer.innerHTML = "<p>An error occurred. Please try again later.</p>";
    }

    // Clear input field
    userSkillsInput.value = "";
});