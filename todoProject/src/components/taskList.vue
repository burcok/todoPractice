<template>
  <ul v-auto-animate class="bg-gray-600 rounded-xl p-10">
    <div class="flex justify-between">
      <span class="font-medium text-3xl">TODO</span>

      <!-- Modal toggle -->
      <button
        data-modal-target="authentication-modal"
        data-modal-toggle="authentication-modal"
        class="block text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-600 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
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
              <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">
                Yeni bir TODO ekle
              </h3>
              <form @submit.prevent="createTask" class="space-y-6" action="#">
                <div>
                  <label
                    for="email"
                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
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
                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
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
                    class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-300"
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
    <li class="mt-6" v-for="task in tasks" :id="'listItem' + task.id">
      <div class="flex items-center">
        <input
          type="checkbox"
          :id="'task' + task.id"
          v-model="task.done"
          @change="updateTaskStatus(task)"
          class="appearance-none h-4 w-4 border rounded-sm bg-white text-black checked:bg-green-600 checked:border-green-600 outline-none duration-500 mr-2"
        />
        <label class="unselectable font-semibold text-lg mr-3" :for="'task' + task.id">
          {{ task.title }}
        </label>
        <label class="unselectable text-gray-900" :for="'task' + task.id">
          {{ task.description }}
        </label>
      </div>
      <hr class="border-gray-700 mt-1 mb-2" />
      <button
        class="duration-500 bg-cyan-900 hover:bg-cyan-700 px-3 font-semibold rounded-md mx-2"
        @click=""
      >
        Düzenle
      </button>
      <button
        class="duration-500 bg-red-900 hover:bg-red-600 px-3 font-semibold rounded-md mx-2"
        @click="deleteTask(task)"
      >
        Sil
      </button>
    </li>
  </ul>
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
        console.log(tasks.value);
      } catch (error) {
        console.error(error);
        setInterval(fetchTasks, 5000);
      }
    };

    const updateTaskStatus = async (task) => {
      try {
        await axios.put(`http://localhost:5000/tasks/${task.id}`, { done: task.done });
        setTimeout(null, 200);
      } catch (error) {
        console.error(error);
      }
    };

    const deleteTask = async (task) => {
      try {
        await axios.delete(`http://localhost:5000/tasks/${task.id}`).then((response) => {
          document.querySelector("#listItem" + response.data.id).remove();
        });
        setTimeout(null, 500);
      } catch (error) {
        console.error(error);
      }
    };

    const createTask = async () => {
      try {
        console.log(title.value, description.value, done.value);
        await axios.post("http://localhost:5000/tasks", {
          title: title.value,
          description: description.value,
          done: done.value,
        });
        setTimeout(fetchTasks, 500);
      } catch (error) {
        console.error(error);
      }
    };

    fetchTasks();

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
