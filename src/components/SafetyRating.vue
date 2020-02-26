<template>
  <div class="ratingBox">
    <h3 align="left"><b>Safety Rating</b></h3>
    <p align="left">
      <b>{{getRating()}}{{rating}}</b>
    </p>
  </div>
</template>

<script>
export default {
    name: 'SafetyRating',
    props: ["country"],
    data(){
        return {
            rating:"huh"
        }
    },
    methods: {
      getRating: function() {
        var Feed = require('rss-to-json');
        Feed.load('https://cors-anywhere.herokuapp.com/https://travel.state.gov/_res/rss/TAsTWs.xml', function(err, rss){
           console.log(rss);
           var a = rss.items;
           console.log(a[70].title);
           return a[70].title
         });
         this.rating = "Japan - Level 2: Exercise Increased Caution"
    }
  } 
}
</script>