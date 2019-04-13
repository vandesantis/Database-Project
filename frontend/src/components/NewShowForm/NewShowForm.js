import React from 'react';



class NewShowForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            title: '',
            synopsis: '',
            genre: '',
            fcc: ''
        }
    }

    onTitleChange = (event) => {
        this.setState({title: event.target.value});
    }

    onSynopsisChange = (event) => {
        this.setState({synopsis: event.target.value});
    }

    onGenreChange = (event) => {
        this.setState({Genre: event.target.value});
    }

    onFccChange = (event) => {
        this.setState({fcc: event.target.value});
    }

    updateDatabase = () => {
        fetch('http://localhost:3000/submitform', {
            method: 'post',
            headers: {'Content-TRype': 'application/json'},
            body: JSON.stringify({
                title: this.state.title,
                synopsis: this.state.synopsis,
                genre: this.state.genre,
                fcc: this.state.fcc
            })
        })
        .then(response => response.json())
    }

    render() {
        return (
            <form class="pa4 black-80">
                <div class="measure center">
                    <label for="title" class="f6 b db mb2">Title</label>
                    <input 
                        id="title" 
                        class="input-reset ba b--black-20 pa2 mb2 db w-100 mb4" 
                        type="text"
                        onChange = {this.onTitleChange}
                        />
                </div>
                <div class="measure center">
                    <label for="synopsis" class="f6 b db mb2">Synopsis</label>
                    <input 
                        id="synopsis" 
                        class="input-reset ba b--black-20 pa2 mb2 db w-100 mb4" 
                        type="text"
                        onChange = {this.onSynopsisChange}
                        />
                </div>
                <div class="measure center">
                    <label for="genre" class="f6 b db mb2">Genre</label>
                    <input 
                        id="genre" 
                        class="input-reset ba b--black-20 pa2 mb2 db w-100 mb4" 
                        type="text"
                        onChange = {this.onGenreChange}
                        />
                </div>
                <div class="measure center">
                    <label for="fcc" class="f6 b db mb2">FCC</label>
                    <input 
                        id="fcc" 
                        class="input-reset ba b--black-20 pa2 mb2 db w-100 mb4"
                         type="text"
                         onChange = {this.onFccChange}
                         />
                </div>
                <div className="">
                    <input 
                        onClick={this.updateDatabase}
                        className="b ph3 pv2 input-reset ba b--black bg-transparent grow pointer f6 dib" 
                        type="submit" 
                        value="Submit"/>
                </div>
            </form>
        );
      }
}

export default NewShowForm;