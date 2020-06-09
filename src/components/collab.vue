<template>
<div>
    <div class="title">
        <h2>{{ this.title }}</h2>
    </div>

    <div>
        <div class="row">
            <div class="col-md-6">
                <textarea  v-model="markdown" name="" id="" cols="80" rows="15" @keyup="postMark"></textarea>
            </div>
            <div id="preview" class="col-md-6" v-html="compiledMarkdown"></div>
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios";
import marked from "marked";
import pusher from "pusher-js";

export default {
name: "collab",
data() {
    return {
    title: "Realtime Markdown Editor",
    markdown: "",
    channel : {}
    };
},
created() {
        let pusher = new Pusher("1016331", {
        cluster: "us2",
        encrypted: true,
        authEndpoint: 'http:/benetravel-dev.s3-website-us-east-1.amazonaws.com/pusher/auth',
        });

        this.channel = pusher.subscribe("private-markdown");
        this.channel.bind("client-new-text", data => {
        this.markdown = data;
        });
    },
computed : {
    compiledMarkdown: function () {
        return marked(this.markdown, { sanitize: true })
    }
    },
    methods: {
          postMark: function(e) {
            const text = e.target.value;
            this.channel.trigger("client-new-text", text);
          },
    }  

};
</script>

<style>
.title {
margin-bottom: 40px;
}
#preview {
border: 2px solid;
text-align: left;
}
</style>
