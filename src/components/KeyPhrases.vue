<template>
  <div class="phraseBox">
    <h3 align="left"><b>Key Phrases in Japanese</b></h3>
    <div v-bind:key="phrase.id" v-for="phrase in phrases">
      <p align="left">
      <b>{{phrase.eng_phrase}} -> {{phrase.trans_phrase}}</b>
      </p>
    </div>
  </div>
</template>

<script>
export default {
    name: 'KeyPhrases',
    props: ["phrases"],
    data(){
        return {
            phrase:"huh"
        }
    }
}
</script>