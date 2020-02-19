<template>
  <div class="ratingBox">
    <h3 align="left">Japan Safety Rating</h3>
    <div v-bind:key="rating.id" v-for="rating in ratings">
      <p align="left">
      {{rating.message}}
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