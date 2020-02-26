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
            rating:"Country not found"
        }
    },
    methods: {
      getRating: function() {
        var Feed = require('rss-to-json');
        var self = this;
        Feed.load('https://cors-anywhere.herokuapp.com/https://travel.state.gov/_res/rss/TAsTWs.xml', function(err, rss){
           console.log(rss);
           var a = rss.items;
           console.log(a[70].title);
           self.rating = a[70].title
         });
    }
  } 
}
</script>