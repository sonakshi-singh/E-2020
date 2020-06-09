<template>
  <div>
    <banner></banner>
          <!--  <GoogleLogin :params="params" :renderParams="renderParams" :onSuccess="onSuccess" :onFailure="onFailure"></GoogleLogin>
           <GoogleLogin :params="params" :logoutButton=true>Logout</GoogleLogin> -->
   
    <div v-if ='edit!=false' >
        <edit v-bind:form="form"></edit>
        <button @click="submit">Submit</button>
    </div>
    <div v-if ='edit!=true' >
        <Template v-bind:form="form"></Template>
         <button @click="back">Go Back!</button>  
    </div>
  </div>
</template>
<script>
import banner from "./banner.vue";
import GoogleLogin from 'vue-google-login';
import Template from "./template.vue";
import edit from "./edit.vue"
import getImageListURL from "../awsCalls/getImageListURL.js"

export default {
    name:"templatePage",
   // props: ['form'],
    data(){
        return {
            edit: true,
            form: {
             title: '',
             value: '',
             text1 : '',
             text2: '',
             image1:'',
             image2:''
        },
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
    created: function() {
      var images = getImageListURL("NickGulson", ["MikeGrad1.jpeg","MikeGrad2.jpeg"])
      this.form.image1 = images[0]
      this.form.image2 = images[1]
     },
    methods: {
        onSuccess(googleUser) {
          console
            console.log(googleUser);
 
            // This only gets the user information: id, name, imageUrl and email
            console.log(googleUser.getBasicProfile());
        },
        back(){
            this.edit = true
        },
        submit(){
            this.edit = false
            console.log(this.edit)
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
        Template,
        edit
    }
};
</script>
