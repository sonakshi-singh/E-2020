<template>
  <div>
    <Banner></Banner>
     <!-- <div v-bind:key="q" v-for="q in questions">
      <p align="left">
      <b-img :src= "q.image"></b-img>
      <input v-model="message" placeholder="type country name here">
      </p> -->
      <div v-if='gameComplete == false' >
        <h1 class='title'>Bene Travel Mania</h1>
        <h2 class="tag"> Guess the country ? </h2>
        <br/>
        <b-img :src=locate class="img"></b-img>
        <br/>
        <div>
        <p class="overlay">  
        <input type="text" v-model='msg' placeholder="type country name here "> 
        <button v-on:click="submit">Submit</button>
        </p>
        </div>
        <h1></h1>
        </div>
        <div v-if='gameComplete == true' class="test" >
        <br> <br/>
        <h1>Thank you for taking the quiz with us</h1>
        
            <h2>Result: {{this.res}}/{{this.num_questions}} </h2>

        <h1></h1>
        </div>
  </div>
</template>


<script>
import Banner from "./Banner.vue";

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
      msg:"",
      res:0,
      num_questions: 4,
      gameComplete: false,
      upperCaseDest: "TOKYO",
      country: "Japan",
      locate:"",

    };
  },
  created() {
    this.question = 0
    this.gameComplete = false
    this.locate=this.questions[0].image
  },
  methods: {
     submit() {
        // this.gameComplete=true;
        
        if(this.question<this.num_questions-1){
            console.log("button clicked",this.question)
            // console.log("HELL",(this.questions[this.question].country).toLowerCase())
            if(this.msg.toLowerCase()==((this.questions[this.question].country).toLowerCase()))
            {
                this.res++;
            }
            this.question++;
            console.log("button clicked",this.question)
            this.locate=this.questions[this.question].image
            // window.location.reload()
        }
        else{
            this.gameComplete=true
        }
        this.msg=
        console.log(this.locate)
        return
    }
  },
  components: {
    Banner
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

.test{
    padding:25px;
    // border:5px solid red;    
}

.title{
    font-style:bold;
}
.img{
    height:400px;
    width:700px;
}

.tag{
    font-style:italic;
}
.overlay{
    
    margin:10px;
    padding:10px;
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

