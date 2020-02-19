<template>
  <div class="ratingBox">
    <h3 align="left"><b>Japan Safety Rating</b></h3>
    <div v-bind:key="rating.id" v-for="rating in ratings">
      <p align="left">
      <b>{{rating.message}}</b>
      </p>
    </div>
  </div>
</template>

<script>
export default {
    name: 'SafetyRating',
    props: ["ratings"],
    data(){
        return {
            rating:"huh"
        }
    }
}
</script>