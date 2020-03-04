<template>
  <div class="phraseBox">
    <h1 align="left">
      <b>Key Phrases in Japanese</b>
    </h1>
    <div v-bind:key="phrase.id" v-for="phrase in phrases">
      <p align="left">
        <b>{{phrase.eng_phrase}} -> {{phrase.trans_phrase}}</b>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "KeyPhrases",
  data() {
    return {
      phrases: [
        { id: 1, eng_phrase: "Hello", trans_phrase: "Konnichiwa" },
        { id: 2, eng_phrase: "Goodbye", trans_phrase: "Sayonara" },
        { id: 3, eng_phrase: "Yes", trans_phrase: "Hai" },
        { id: 4, eng_phrase: "No", trans_phrase: "Lie" },
        { id: 5, eng_phrase: "Please", trans_phrase: "Onegaishimasu" },
        { id: 6, eng_phrase: "Thank You", trans_phrase: "Domo Arigato" }
      ],
      phrase: "",
      destination: ""
    };
  },
  created() {
    this.testItOut();
  },
  methods: {
    testItOut() {
      this.$root.$on("destWasEntered", travel => {
        this.destination = travel;
        console.log("WAIT WHAT", this.destination);
      });
    }
  }
};
</script>