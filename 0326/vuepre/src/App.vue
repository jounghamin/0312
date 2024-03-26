<!-- <template>
  <div>
    <h1 :id ="myid" :class="myClass">{{ text }}</h1>
  </div>
</template>

<script setup>
const text = 'hello world!'
const myid = 'header'
const myClass = ['bold', 'color' , 'size']
</script>

<style lang="scss" scoped>
.bold {
  font-weight: bold;
}
.color {
  color: blueviolet;
}
.size {
  font-size: 5rem;
}
</style> -->


<!-- <template>
  <div>
    <button @click="alertText">클릭!</button>
    <form action="">
      <input type="text">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>

function alertText() {
  alert('Hello, World!');
}
</script> -->

<!-- 
<template>
  <div>
    <div>{{ count }}, {{ state.count }}</div>
    <button @click="increment">클릭!</button>
    <button @click="incrementState">클릭!</button>

  </div>
</template>
프로세스
1. input에 입력을 한다
2. 입력에 대한 event 가 발생
3. event 에서 입력 값을 가져올 수 있다.  -->
<!-- <script setup>
import { ref, reactive } from 'vue';
const count = ref(0);
const state = reactive({
  count: 0
});

function increment() {
  count.value++;
}
function incrementState() {
  state.count++;
}

</script> --> -->

<!-- v -model -->
<template>
  <div>
    <input v-model="text">
    <p>{{ text }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const text = ref('')
</script>