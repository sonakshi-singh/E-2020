<template>
  <div>
    <b-container fluid="" class="template-container" >
      <br>
      <br><br><br><br><br><br><br><br><br><br>
           <input  :value="this.title" class = "title" placeholder ="text" >
          <b-row align-h="center">
            <b-col cols="4">
            <img :src="this.images[0]" class="ret"  >
            </b-col><b-col cols="4">
            <input  :value="this.messages[0]" class = "txt" placeholder ="text" @change="messageChange" >
            </b-col>
            </b-row >
          <b-row align-h="center">
            <b-col cols="4">
               <input  :value="this.messages[1]" class = "txt" placeholder ="text" >
            </b-col><b-col cols="4">
              <img :src="this.images[1]" class="ret"  >
          </b-col></b-row>
          </b-container>
  </div>
</template>

<script>
import getImageListURL from "../awsCalls/getImageListURL.js"
export default {
    name:"template",
    data(){
        return {
            title: "title",
            images: [],
            messages: []
        }
    },
    methods: {
      messageChange(event){
        console.log(event)
        console.log(this.images)
      }
    },
    components: {
    },
    created: function() {
      this.images = getImageListURL("NickGulson", ["MikeGrad1.jpeg","MikeGrad2.jpeg"])
      console.log(this.images)
  }
};
</script>

<style lang="scss" scoped>
.template-container {
    padding-top : 5%;
    background-image: url("../assets/gradBackground.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    min-height: 90%;
}
.txt {
    width: 200px;
    height :300px;
} 
.ret{
    width: 300px;
    height :400px;
    padding:20px;
}
</style>