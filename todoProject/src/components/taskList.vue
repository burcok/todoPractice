<template>
  <div v-auto-animate class="bg-gray-600 border-gray-700 shadow-2xl rounded-xl p-10">
    <div class="flex justify-center flex-wrap md:justify-between">
      <span class="font-bold text-3xl mx-10">TODO</span>

      <!-- Modal toggle -->
      <button
        data-modal-target="authentication-modal"
        data-modal-toggle="authentication-modal"
        class="block shadow-xl text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-600 font-medium rounded-lg text-sm mt-7 md:mt-0 px-5 py-2 md:px-5 md:py-2.5 text-center"
        type="button"
      >
        Yeni TODO Ekle
      </button>

      <!-- Main modal -->
      <div
        id="authentication-modal"
        tabindex="-1"
        aria-hidden="true"
        class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-modal md:h-full"
      >
        <div class="relative w-full h-full max-w-md md:h-auto">
          <!-- Modal content -->
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <button
              type="button"
              class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
              data-modal-hide="authentication-modal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
            <div class="px-6 py-6 lg:px-8">
              <h3
                class="unselectable mb-4 text-xl font-medium text-gray-900 dark:text-white"
              >
                Yeni bir TODO ekle
              </h3>
              <form @submit.prevent="createTask" name="createTaskForm" class="space-y-6">
                <div>
                  <label
                    for="title"
                    class="unselectable block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Başlık</label
                  >
                  <input
                    type="text"
                    name="title"
                    id="title"
                    v-model="title"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Learn Javascript"
                    required
                  />
                </div>
                <div>
                  <label
                    for="description"
                    class="unselectable block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Açıklama</label
                  >
                  <input
                    type="text"
                    name="description"
                    id="description"
                    v-model="description"
                    placeholder="Need to find a good Javascript tutorial"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    required
                  />
                </div>
                <div class="flex items-start">
                  <div class="flex items-center h-5">
                    <input
                      id="remember"
                      type="checkbox"
                      value=""
                      v-model="done"
                      class="w-4 h-4 border border-gray-500 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800"
                    />
                  </div>
                  <label
                    for="remember"
                    class="unselectable ml-2 text-sm font-medium text-gray-700 dark:text-gray-300"
                    >Tamamlandı</label
                  >
                </div>
                <button
                  type="submit"
                  data-modal-hide="authentication-modal"
                  class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                >
                  EKLE
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ul v-auto-animate id="todoList">
      <li
        class="duration-700 border-gray-600/60 even:border-gray-700/90 even:bg-gray-700/50 rounded-md p-8 md:p-3 mt-6"
        v-for="task in tasks"
      >
        <div class="flex items-center">
          <input
            type="checkbox"
            :id="'listItem' + task.id"
            v-model="task.done"
            @change="updateTaskStatus(task)"
            class="appearance-none h-4 w-4 border rounded-sm bg-white text-black checked:bg-green-600 checked:border-green-600 outline-none duration-500 mr-2"
          />
          <div class="flex flex-wrap md:inline-block">
            <label
              class="unselectable font-semibold text-lg mr-3"
              :for="'listItem' + task.id"
            >
              {{ task.title }}
            </label>
            <label class="unselectable text-gray-900" :for="'listItem' + task.id">
              {{ task.description }}
            </label>
          </div>
        </div>
        <hr class="border-gray-700 mt-1 mb-2" />
        <button
          class="duration-500 w-full md:w-20 bg-cyan-900 hover:bg-cyan-700 px-3 font-semibold rounded-md my-3 md:my-0 md:mx-2"
          @click=""
        >
          Düzenle
        </button>
        <button
          class="duration-500 w-full md:w-20 bg-red-900 hover:bg-red-600 px-3 font-semibold rounded-md md:mx-2"
          @click="deleteTask(task)"
        >
          Sil
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  setup() {
    const tasks = ref([]);
    const title = ref("");
    const description = ref("");
    const done = ref(false);

    const fetchTasks = async () => {
      try {
        const response = await axios.get("http://localhost:5000/tasks");
        tasks.value = response.data.tasks;
      } catch (error) {
        console.error(error);
        setTimeout(fetchTasks, 10000);
      }
    };

    const updateTasks = async () => {
      await fetchTasks();
      let todoList = document.querySelector("#todoList").children;
      for (let i = 0; todoList.length > i; i++) {
        let checkTaskCheckbox = todoList[i];
        let checkTask = tasks.value[i].done;
        if (checkTask == true) {
          checkTaskCheckbox.classList.add("shadow-none");
          checkTaskCheckbox.classList.remove("shadow-md");
        } else {
          checkTaskCheckbox.classList.add("shadow-md");
          checkTaskCheckbox.classList.remove("shadow-none");
        }
      }
    };

    const updateTaskStatus = async (task) => {
      try {
        await axios.put(`http://localhost:5000/tasks/${task.id}`, { done: task.done });
        updateTasks();
      } catch (error) {
        console.error(error);
      }
      updateTasks;
    };

    const deleteTask = async (task) => {
      try {
        await axios.delete(`http://localhost:5000/tasks/${task.id}`);
        updateTasks();
        // checkAndDeleteTask(task);
      } catch (error) {
        console.error(error);
      }
    };

    // const checkAndDeleteTask = async (task) => {
    //   const taskItem = [...document.querySelectorAll("li")];
    //   for (let i = 0; taskItem.length > i; i++) {
    //     if (taskItem[i].id == "listItem" + task.id) {
    //       taskItem[i].remove();
    //     }
    //   }
    // };

    const createTask = async () => {
      try {
        await axios.post("http://localhost:5000/tasks", {
          title: title.value,
          description: description.value,
          done: done.value,
        });
        updateTasks();
      } catch (error) {
        console.error(error);
      }
      description.value = "";
      title.value = "";
      done.value = false;
    };

    updateTasks();

    return {
      tasks,
      updateTaskStatus,
      deleteTask,
      createTask,
      title,
      description,
      done,
    };
  },
};
</script>
