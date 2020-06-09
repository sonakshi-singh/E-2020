<template>
  <div>
    <banner></banner>
    <h1>Template</h1>
            <GoogleLogin :params="params" :renderParams="renderParams" :onSuccess="onSuccess" :onFailure="onFailure"></GoogleLogin>
            <GoogleLogin :params="params" :logoutButton=true>Logout</GoogleLogin>
    <Template></Template>
  </div>
</template>
<script>
import banner from "./banner.vue";
import GoogleLogin from 'vue-google-login';
import Template from "./template.vue";

export default {
    name:"templatePage",
    data(){
        return {
            title: "",
            images: [],
            messages: [],
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
        banner,
        GoogleLogin,
        Template
    }
};
</script>
