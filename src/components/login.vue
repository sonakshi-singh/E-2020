<template>
  <div>
    <!-- <banner></banner> -->
    <b-container fluid class="login-container">
      <div class="wrapper">
        <div class="container">
          <div class="row">
            <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
              <div class="card card-signin my-5">
                <div class="card-body">
                  <h5 class="card-title text-center">Welcome to Bene</h5>
                  <form class="form-signin">
                    <div class="form-label-group">
                      <input
                        type="email"
                        id="inputEmail"
                        class="form-control"
                        placeholder="Email address"
                        required
                        autofocus
                      />
                      <!-- <label for="inputEmail">Email address</label> -->
                    </div>

                    <div class="form-label-group">
                      <input
                        type="password"
                        id="inputPassword"
                        class="form-control"
                        placeholder="Password"
                        required
                      />
                      <!-- <label for="inputPassword">Password</label> -->
                    </div>

                    <div class="custom-control custom-checkbox mb-3">
                      <input type="checkbox" class="custom-control-input" id="customCheck1" />
                      <label class="custom-control-label" for="customCheck1">Remember password</label>
                    </div>
                    <button
                      class="btn btn-lg btn-primary btn-block text-uppercase"
                      type="submit"
                    >Sign in</button>
                    <hr class="my-4" />
                    <div class="google-login">
                      <GoogleLogin
                        :params="params"
                        :renderParams="renderParams"
                        :onSuccess="onSuccess"
                        :onFailure="onFailure"
                      ></GoogleLogin>
                    </div>
                    <!-- <button class="btn btn-lg btn-google btn-block text-uppercase" type="submit">
                      <i class="fab fa-google mr-2"></i> Sign in with Google
                    </button>-->
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </b-container>
  </div>
</template>


<script>
import GoogleLogin from "vue-google-login";
import gallery from './gallery.vue';
import { bus } from '../main'
export default {
  name: "login",
  data() {
    return {
      googleCreds: "",
      params: {
        client_id:
          "991176984652-n9j3cc8mk83kgc2tc6hn0i1ubcpt3qod.apps.googleusercontent.com"
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
    this.res = 0;
    this.locate = this.questions[0].image;
    for (var i = 0; i < this.num_questions; i++) {
      this.correct[i] = [i, false];
    }
  },
  methods: {
    onSuccess(googleUser) {
      console.log("whatwhat", googleUser);
      this.googleCreds = googleUser.getBasicProfile();
      // This only gets the user information: id, name, imageUrl and email
      if (this.$root.$emit('passingCreds', this.googleCreds)) {
        console.log(this.googleCreds)
        this.$router.push({ name: "gallery" });
      }
    },
    onFailure(error) {
      console.log(error);
      // This only gets the user information: id, name, imageUrl and email
      // console.log(googleUser.getBasicProfile());
    }
  },
  
  components: {
    GoogleLogin,
    gallery
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
.login-container {
  background-image: url("../assets/login_background.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
  min-height: 100%;
}
/**** TYPEWRITER EFFECT  ******/
.typewriter {
  margin: 4em 0 0 0;
  h1 {
    display: inline-block;
    overflow: hidden;
    letter-spacing: 2px;
    animation: typing 2s steps(60, end), blink 0.75s step-end infinite;
    white-space: nowrap;
    font-size: 45px;
    font-weight: 400;
    color: black;
    // border-right: 4px solid orange;
    box-sizing: border-box;
    // overflow: hidden; /* Ensures the content is not revealed until the animation */
    // border-right: 0.15em solid orange; /* The typwriter cursor */
    // white-space: nowrap; /* Keeps the content on a single line */
    // margin: 0 auto; /* Gives that scrolling effect as the typing happens */
    // letter-spacing: 0.15em; /* Adjust as needed */
    // animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
  }
}
/* The typing effect */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}
/* The typewriter cursor effect */
@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }
  50% {
    border-color: orange;
  }
}
/***** LOGIN STYLING  ******/
.card-signin {
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
}
.card-signin .card-title {
  margin-bottom: 2rem;
  font-weight: 800;
  font-size: 1.5rem;
}
.card-signin .card-body {
  padding: 2rem;
}
.form-signin {
  width: 100%;
}
.form-signin .btn {
  font-size: 80%;
  border-radius: 5rem;
  letter-spacing: 0.1rem;
  font-weight: bold;
  padding: 1rem;
  transition: all 0.2s;
  background-color: #b3d9f2
}
.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}
.form-label-group input {
  height: auto;
  border-radius: 2rem;
}
.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0;
  /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  border: 1px solid transparent;
  border-radius: 0.25rem;
  transition: all 0.1s ease-in-out;
}
.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}
.form-label-group input:-ms-input-placeholder {
  color: transparent;
}
.form-label-group input::-ms-input-placeholder {
  color: transparent;
}
.form-label-group input::-moz-placeholder {
  color: transparent;
}
.form-label-group input::placeholder {
  color: transparent;
}
.form-label-group input:not(:placeholder-shown) {
  padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
  padding-bottom: calc(var(--input-padding-y) / 3);
}
.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: calc(var(--input-padding-y) / 3);
  padding-bottom: calc(var(--input-padding-y) / 3);
  font-size: 12px;
  color: #777;
}
.google-login {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
