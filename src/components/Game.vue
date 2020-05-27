<template>
  <div>
    <Banner></Banner>
    <div v-bind:key="q" v-for="q in questions">
      <p align="left">
      <b-img :src= "q.image"></b-img>
      <input v-model="message" placeholder="type country name here">
      </p>
    </div>
  </div>
</template>


<script>
import Banner from "./Banner.vue";
import GoogleLogin from 'vue-google-login';

export default {
  name: "Game",
  data() {
    return {
        questions: [
        { country: "Thailand", image: "https://i.imgur.com/bCcNhRS.png" },
        { country: "Hong Kong", image: "https://i.imgur.com/EpfJGWQ.png" },
        { country: "China", image: "https://i.imgur.com/BjnarRv.png" },
        { country: "Singapore", image: "https://i.imgur.com/49AbYZB.png" }
        ], 
      question: 0,
      num_questions: 4,
      gameComplete: false,
      upperCaseDest: "TOKYO",
      country: "Japan",
      params: 
      {
          client_id: "991176984652-n9j3cc8mk83kgc2tc6hn0i1ubcpt3qod.apps.googleusercontent.com"
      },
                // only needed if you want to render the button with the google ui
      renderParams: {
          width: 250,
          height: 50,
          longtitle: true
      }
    }
  },
  created() {
    this.question = 0
    this.gameComplete = false
  },
  methods: {
    
  },
  components: {
    Banner,
    GoogleLogin
  }
};
</script>

<style lang="scss" scoped>
@mixin font-weight($font-weight) {
  font-weight: $font-weight;
  text-align: left;
}
* {
  font-family: "Montserrat", sans-serif;
  color: #333;
  text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);
}

html,
body {
  height: 100%;
}

.factSheet-container {
  margin: 1em 0 0 0;

  .download {
    color: white;
  }

  .tokyo-heading {
    @include font-weight(800);
    letter-spacing: 2px;
  }

  .country-info {
    margin: 1em 0 0 0;
  }

  .heading {
    margin: 2em 0 0 0;
    @include font-weight(600);
  }

  .content {
    margin: 0.5em 0 0 0;
    @include font-weight(400);
    display: list-item; /* This has to be "list-item"                                               */
    list-style-type: disc; /* See https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type     */
    list-style-position: inside;
  }

  hr {
    border-color: lightgray transparent #474747 transparent;

    border-style: solid;
    height: 0;
  }
}
</style>

