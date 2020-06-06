<template>
  <div>
    <Banner></Banner>
        <GoogleLogin id ="test" :params="params" :onSuccess="onSuccess" :onFailure="onFailure">Login</GoogleLogin> 
        <GoogleLogin :params="params" :renderParams="renderParams" :onSuccess="onSuccess" :onFailure="onFailure"></GoogleLogin>
        <GoogleLogin :params="params" :logoutButton=true>Logout</GoogleLogin>
        </div>
</template>


<script>
import Banner from "./Banner.vue";
import GoogleLogin from 'vue-google-login';


export default {
  name: "login",
  data() {
    return {
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

#test{
  color:red;
  // background-color:red;
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

