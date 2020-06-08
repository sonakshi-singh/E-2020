<template>
  <div>
    <b-container fluid="" class="template-container" >
      <br>
      <br><br><br><br><br><br>

      <img src= this.images[0] >
      <input  :value="this.messages[0]" placeholder ="text" @change="messageChange" >
      <img src= this.images[1] >
      <input  :value="this.messages[1]" placeholder ="text" >
    </b-container>
  </div>
</template>

<script>
import getImageList from "../awsCalls/getImageList.js"

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
      this.images = getImageList(["NickGulson/MikeGrad1.jpeg","NickGulson/MikeGrad2.jpeg"])
      console.log(this.images)
  }
};
</script>

<style lang="scss" scoped>
.template-container {
    padding-top: 100%;
    background-image: url("../assets/gradBackground.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    min-height: 90%;
}
</style>
