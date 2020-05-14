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
    axios.get(`/images?offset=${offset}`).then((res) => {
      this.setState({ images: res.data, offset: 4 });
    });
  }

  fetchImages = () => {
    const { offset } = this.state;
    axios.get(`/images?offset=${offset}`).then((res) => {
      this.setState({
        images: this.state.images.concat(res.data),
        offset: offset + 5,
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
