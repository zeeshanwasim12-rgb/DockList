const addForm    = document.getElementById("add-form");
const taskInput  = document.getElementById("task-input");
const taskList   = document.getElementById("task-list");
const message    = document.getElementById("message");
const filters    = document.getElementById("filters");
const emptyState = document.getElementById("empty-state");
const taskCount  = document.getElementById("task-count");


let allTasks = [];       
let currentFilter = "all"; 

function showMessage(text) {
  message.textContent = text;
  message.classList.toggle("message--visible", Boolean(text));
  message.classList.toggle("message--error", Boolean(text));
}

async function loadTasks() {
  try {
    const response = await fetch("/api/tasks");
    allTasks = await response.json();
    render();
  } catch (err) {
    showMessage("Could not load tasks. Is the server running?");
  }
}

function render() {

  let visible = allTasks;
  if (currentFilter === "active") {
    visible = allTasks.filter((t) => !t.completed);
  } else if (currentFilter === "completed") {
    visible = allTasks.filter((t) => t.completed);
  }

  taskList.innerHTML = "";
  emptyState.style.display = visible.length === 0 ? "block" : "none";

  visible.forEach((task) => {
    const li = document.createElement("li");
    li.className = "task" + (task.completed ? " task--done" : "");

    const toggle = document.createElement("button");
    toggle.className = "task__toggle";
    toggle.setAttribute("aria-label", "Toggle complete");
    toggle.textContent = task.completed ? "✓" : "";
    toggle.addEventListener("click", () => toggleTask(task.id));

    const title = document.createElement("span");
    title.className = "task__title";
    title.textContent = task.title;

    const del = document.createElement("button");
    del.className = "task__delete";
    del.setAttribute("aria-label", "Delete task");
    del.textContent = "✕";
    del.addEventListener("click", () => deleteTask(task.id));

    li.appendChild(toggle);
    li.appendChild(title);
    li.appendChild(del);
    taskList.appendChild(li);
  });

  const active = allTasks.filter((t) => !t.completed).length;
  taskCount.textContent = `${allTasks.length} task(s) · ${active} active`;
}

addForm.addEventListener("submit", async (event) => {
  event.preventDefault(); 

  const title = taskInput.value.trim();

  if (!title) {
    showMessage("Please type a task before adding.");
    return;
  }

  try {
    const response = await fetch("/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: title }),
    });

    if (!response.ok) {
      const data = await response.json();
      showMessage(data.error || "Something went wrong.");
      return;
    }

    taskInput.value = ""; 
    showMessage("");    
    await loadTasks();   
  } catch (err) {
    showMessage("Could not add task. Is the server running?");
  }
});

async function toggleTask(id) {
  try {
    await fetch(`/complete/${id}`, { method: "POST" });
    await loadTasks();
  } catch (err) {
    showMessage("Could not update task.");
  }
}

async function deleteTask(id) {
  try {
    await fetch(`/delete/${id}`, { method: "POST" });
    await loadTasks();
  } catch (err) {
    showMessage("Could not delete task.");
  }
}

filters.addEventListener("click", (event) => {
  if (!event.target.matches(".filters__btn")) return;

  currentFilter = event.target.dataset.filter;

  document.querySelectorAll(".filters__btn").forEach((btn) => {
    btn.classList.toggle("is-active", btn === event.target);
  });

  render(); 
});

loadTasks();
