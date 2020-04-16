import React, { Component } from "react";
import axios from "axios";
import InfiniteScroll from "react-infinite-scroll-component";
import Image from "./image";

export class Images extends Component {
  constructor() {
    super();
    this.state = {
      images: [],
      offset: 1,
    };
    this.fetchImages = this.fetchImages.bind(this);
  }

  componentDidMount() {
    const { offset } = this.state;
    console.log(this.state);
    axios.get(`/images?offset=${offset}`).then((res) => {
      this.setState({ images: res.data, offset: 9 });
      console.log("This state after mount fetch");
      console.log(this.state);
    });
  }

  fetchImages = () => {
    console.log(this.state);
    const { offset } = this.state;
    axios.get(`/images?offset=${offset}`).then((res) => {
      this.setState({
        images: this.state.images.concat(res.data),
        offset: offset + 10,
      });
    });
  };

  render() {
    return (
      // <div>Hello</div>
      <div className="images">
        <InfiniteScroll
          dataLength={this.state.images.length}
          next={this.fetchImages}
          hasMore={true}
          loader={<h3>...</h3>}
        >
          {this.state.images.map((image) => (
            <Image key={image.uuid} image={image} />
          ))}
        </InfiniteScroll>
      </div>
    );
  }
}

export default Images;