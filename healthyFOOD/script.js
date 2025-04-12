const app = document.getElementById("app");

let step = 0;
const formData = {
  name: "",
  age: "",
  weight: "",
  diseases: [],
  exercise: "",
  sleep: ""
};

const diseaseOptions = ["Diabetes", "Hypertension", "PCOS", "None"];
const exerciseOptions = ["0 days", "1-2 days", "3-4 days", "5-7 days"];
const sleepOptions = ["<5 hours", "5-7 hours", "7-9 hours", ">9 hours"];

function render() {
  const nextButton = (disabled = false) => `<button id="nextBtn" class="mt-4 w-full bg-indigo-600 text-white p-2 rounded-md" ${disabled ? 'disabled' : ''}>Next</button>`;
  const backNextButtons = (nextDisabled = false) => `
    <div class="flex justify-between mt-4">
      <button onclick="prevStep()" class="bg-gray-300 p-2 rounded-md">Back</button>
      <button id="nextBtn" class="bg-indigo-600 text-white p-2 rounded-md" ${nextDisabled ? 'disabled' : ''}>Next</button>
    </div>
  `;

  switch(step) {
    case 0:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">Welcome! What's your name?</h2>
        <input type="text" id="nameInput" class="w-full p-2 rounded-md border" placeholder="Enter your name" />
        ${nextButton(!formData.name)}
      `;
      setTimeout(() => {
        const nameInput = document.getElementById('nameInput');
        const nextBtn = document.getElementById('nextBtn');
        nameInput.value = formData.name;
        nameInput.addEventListener('input', (e) => {
          formData.name = e.target.value;
          nextBtn.disabled = !formData.name;
        });
        nextBtn.addEventListener('click', nextStep);
        nameInput.focus();
      });
      break;
    case 1:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">How old are you?</h2>
        <input type="number" id="ageInput" class="w-full p-2 rounded-md border" placeholder="Enter your age" />
        ${backNextButtons(!formData.age)}
      `;
      setTimeout(() => {
        const ageInput = document.getElementById('ageInput');
        const nextBtn = document.getElementById('nextBtn');
        ageInput.value = formData.age;
        ageInput.addEventListener('input', (e) => {
          formData.age = e.target.value;
          nextBtn.disabled = !formData.age;
        });
        nextBtn.addEventListener('click', nextStep);
        ageInput.focus();
      });
      break;
    case 2:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">What's your weight (kg)?</h2>
        <input type="number" id="weightInput" class="w-full p-2 rounded-md border" placeholder="Enter your weight" />
        ${backNextButtons(!formData.weight)}
      `;
      setTimeout(() => {
        const weightInput = document.getElementById('weightInput');
        const nextBtn = document.getElementById('nextBtn');
        weightInput.value = formData.weight;
        weightInput.addEventListener('input', (e) => {
          formData.weight = e.target.value;
          nextBtn.disabled = !formData.weight;
        });
        nextBtn.addEventListener('click', nextStep);
        weightInput.focus();
      });
      break;
    case 3:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">Do you have any of the following conditions?</h2>
        <div class="grid grid-cols-2 gap-3">
          ${diseaseOptions.map(option => `
            <button onclick="toggleMultiSelect('diseases', '${option}')" class="p-2 rounded-md border ${formData.diseases.includes(option) ? 'bg-indigo-600 text-white' : ''}">${option}</button>
          `).join('')}
        </div>
        ${backNextButtons(false)}
      `;
      setTimeout(() => {
        document.getElementById('nextBtn').addEventListener('click', nextStep);
      });
      break;
    case 4:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">How often do you exercise?</h2>
        <div class="grid grid-cols-2 gap-3">
          ${exerciseOptions.map(option => `
            <button onclick="updateForm('exercise', '${option}')" class="p-2 rounded-md border ${formData.exercise === option ? 'bg-indigo-600 text-white' : ''}">${option}</button>
          `).join('')}
        </div>
        ${backNextButtons(!formData.exercise)}
      `;
      setTimeout(() => {
        document.getElementById('nextBtn').addEventListener('click', nextStep);
      });
      break;
    case 5:
      app.innerHTML = `
        <h2 class="text-xl font-semibold mb-4">How many hours do you sleep daily?</h2>
        <div class="grid grid-cols-2 gap-3">
          ${sleepOptions.map(option => `
            <button onclick="updateForm('sleep', '${option}')" class="p-2 rounded-md border ${formData.sleep === option ? 'bg-indigo-600 text-white' : ''}">${option}</button>
          `).join('')}
        </div>
        <div class="flex justify-between mt-4">
          <button onclick="prevStep()" class="bg-gray-300 p-2 rounded-md">Back</button>
          <button onclick="submitForm()" class="bg-green-600 text-white p-2 rounded-md" ${!formData.sleep ? 'disabled' : ''}>Submit</button>
        </div>
      `;
      break;
    case 6:
      app.innerHTML = `
        <div class="text-center">
          <h2 class="text-2xl font-bold mb-4">Welcome ${formData.name}!</h2>
          <p class="text-gray-700">You’ve successfully completed onboarding.</p>
          <a href="/features.html" class="inline-block mt-6 bg-blue-600 text-white p-3 rounded-md">Go to Feature Dashboard</a>
        </div>
      `;
      break;
  }
}

function updateForm(field, value) {
  formData[field] = value;
  render();
}

function toggleMultiSelect(field, value) {
  const index = formData[field].indexOf(value);
  if (index > -1) {
    formData[field].splice(index, 1);
  } else {
    formData[field].push(value);
  }
  render();
}

function nextStep() {
  step++;
  render();
}

function prevStep() {
  step--;
  render();
}

function submitForm() {
  console.log("Submitted Data:", formData);
  step++;
  render();
}

render();