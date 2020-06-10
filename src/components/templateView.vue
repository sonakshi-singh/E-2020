<template>
  
    <b-container fluid="" class="template-container" >
      <div class="grid">
      <br>
      <br><br><br><br><br><br>
       <figure class="fig fig--1" style="--aspect-ratio: 3/4;">
      <img src= this.images[0] >
      </figure>
      <input  :value="this.messages[0]" placeholder ="text" @change="messageChange" id="ip1" ><br>
      <figure class="fig fig--2" style="--aspect-ratio: 4/3;">
      <img src= this.images[1] >
      </figure>
      <input  :value="this.messages[1]" placeholder ="text" id="ip2" >
     </div>
    </b-container>
  
</template>

<script>
// export default {
//   name: "template",
//   data() {
//     return {
//       title: "title",
//       images: [],
//       messages: []
//     };
//   },
//   methods: {
//     messageChange(event) {
//       console.log(event);
//       console.log(this.images);
//     }
//   },
//   components: {},
//   created: function() {
//     this.images = [
//       "https://beneimages.s3.us-east-2.amazonaws.com/NickGulson/MikeGrad1.jpeg",
//       "https://beneimages.s3.us-east-2.amazonaws.com/NickGulson/MikeGrad2.jpeg"
//     ];
//     console.log(this.images);
import getImageListURL from "../awsCalls/getImageListURL.js"
import getImageURL from "../awsCalls/getImageURL.js"

export default {
    name:"templateView",
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
      this.images = getImageURL(["NickGulson/MikeGrad1.jpeg","NickGulson/MikeGrad2.jpeg"])
      console.log(this.images)
  }
};
</script>

<style lang="scss" scoped>
* {
	box-sizing: border-box;
}
.template-container {
  
    background-image: url("../assets/gradBackground.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
  min-height: 10%;
}
figure {
	margin: 0;
	background: rgba(lightBlue, 0.8);
	box-shadow: -0.035rem 0.03rem 0.3rem rgba(0, 0, 0, 0.2);
}
img {
	object-fit: cover;
	width: 100%;
	height: 100%;
	display: block;
}
.grid {
	--verticalPadding: 2rem;
	--overlap: 6rem;
	display: grid;
	/* 6/5 grid from my compound grid generator: https://codepen.io/michellebarker/full/zYOMYWv */
	grid-template-columns: 5fr 1fr 4fr 2fr 3fr 3fr 2fr 4fr 1fr 5fr;
	grid-template-rows: 
		[header-start]
		auto
		[fig1-start]
		3rem
		[header-end]
		minmax(var(--verticalPadding), auto)
		[p1-start]
		minmax(0, auto)
		[p1-end]
		minmax(var(--verticalPadding), auto) 
		[fig2-start]
		var(--overlap) 
		[fig1-end]
		minmax(var(--verticalPadding), auto)
		[p2-start]
		minmax(0, auto)
		[p2-end]
		minmax(var(--verticalPadding), auto)
		[fig3-start]
		var(--overlap)
		[fig2-end]
		minmax(var(--verticalPadding), auto)
		[p3-start]
		minmax(0, auto)
		[p3-end]
		minmax(var(--verticalPadding), auto)
		[fig3-end];
	grid-auto-rows: minmax(var(--verticalPadding), auto);
	gap: 1rem;
	max-width: 75rem;
	margin: 0 auto;
	align-items: center;
	
	
	&::before,
	&::after {
		content: '';
		display: block;
	}
	
	&::before {
		
		grid-column: 3 / -3;
		grid-row: 9 / span 4;
		width: 100%;
  	height: 400px;
		position: relative;
 	 z-index: 2;
	}
}
.fig {
	&--1 {
		grid-column: span 5 / -1;
		grid-row: fig1;
	}
	
	&--2 {
		grid-column: 1 / span 7;
		grid-row: fig2;
	}
	
	&--3 {
		grid-column: span 5 / -2;
		grid-row: fig3;
		
		img {
			object-position: left;
		}
	}
}
input {
	&:first-of-type {
		grid-column: 3 / span 4;
		grid-row: p1;
		z-index: 1;
		transform: rotate(-1deg);
	}
	
	&:nth-of-type(2) {
		grid-column: span 3 / -3;
		grid-row: p2;
		transform: rotate(0.8deg);
	}
	
	&:nth-of-type(3) {
		grid-column: 2 / span 4;
		grid-row: p3;
		transform: rotate(-0.7deg);
	}
}


/* Aspect ratio – https://css-tricks.com/aspect-ratio-boxes/ */
[style*="--aspect-ratio"] {
	position: relative;
}

[style*="--aspect-ratio"]::before {
	content: "";
	display: block;
	padding-bottom: calc(100% / (var(--aspect-ratio)));
}  

[style*="--aspect-ratio"] > :first-child {
	position: absolute;
	top: 0;
	left: 0;
	height: 100%;
} 
</style>
