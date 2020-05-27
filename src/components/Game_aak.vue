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
            <div v-bind:key="q" v-for="q in correct" class="factSheet-container">
              <div v-if='q[1]==true'>
                Correct: {{questions[q[0]].country}}
                <b-img :src='questions[q[0]].image' class="small_img"></b-img>
                <router-link :to="'factSheet'">
                  <button v-on:click="submit">Plan a trip?</button>
                </router-link>
              </div>
              <div v-if='q[1]==false'>
                Incorrect: {{questions[q[0]].country}}
                <b-img :src='questions[q[0]].image' class="small_img"></b-img>
                <router-link :to="'factSheet'">
                  <button v-on:click="submit">Plan a trip?</button>
                </router-link>
              </div>
            </div>
        <h1></h1>
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
        { country: "Singapore", image: "https://i.imgur.com/49AbYZB.png" },
        { country: "Japan", image: "https://i.imgur.com/j0ccf4R.png" }
       ],
      correct: [], 
      question: 0,
      msg:"",
      res:0,
      num_questions: 5,
      gameComplete: false,
      upperCaseDest: "TOKYO",
      country: "Japan",
      locate:"",
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

    };
  },
  created() {
    this.question = 0
    this.gameComplete = false
    this.res = 0
    this.locate=this.questions[0].image
    for (var i=0; i<this.num_questions; i++){
      this.correct[i] = [i,false]
    }
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
                this.correct[this.question][1] = true
                console.log("correct")
            }
            this.question++;
            console.log("button clicked",this.question)
            this.locate=this.questions[this.question].image
            // window.location.reload()
        }
        else{
          if(this.msg.toLowerCase()==((this.questions[this.question].country).toLowerCase()))
            {
                this.res++;
                this.correct[this.question][1] = true
            }
            this.gameComplete=true
        }
        this.msg=
        console.log(this.locate)
        return
    },
    onSuccess(googleUser) {
          console
            console.log(googleUser);
 
            // This only gets the user information: id, name, imageUrl and email
            console.log(googleUser.getBasicProfile());
        },
        onFailure(error) {
            console.log(error);
 
            // This only gets the user information: id, name, imageUrl and email
            // console.log(googleUser.getBasicProfile());
        }
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
.small_img{
    height:120px;
    width:210px;
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
  text-align: left;

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

