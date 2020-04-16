import React from "react";

export default function Image({ image }) {
  return (
    <div class="image-box">
      <p class="image-author"> u/{image.author} </p>
      <img class="single-photo" src={image.image_url} alt="" />
      <p class="image-title"> {image.title} </p>
      <p class="reddit-link">View on Reddit</p>
    </div>
  );
}
