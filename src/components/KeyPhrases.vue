<template>
  <div class="phraseBox">
    <h3 align="left">Key Phrases in Japanese</h3>
    <div v-bind:key="phrase.id" v-for="phrase in phrases">
      <p align="left">
      {{phrase.eng_phrase}} -> {{phrase.trans_phrase}}
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