class Register extends Component {
  constructor(props){
      super(props);
      this.state = {
          username: "",
          email: "",
          password: "",
          password2: "",
      };
      this.handleSubmit = this.handleSubmit.bind(this);
      this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event){
      const target = event.target;
      this.setState({
          [target.name]: target.value,
      });
  }
  handleSubmit(event){
      event.preventDefault();
      /*
      여기에 입력받은 값들 API 전송!!
      */
     axios
      .post("http://localhost:8000/users/register", {
          username: this.state.username,
          email: this.state.email,
          password: this.state.password,
          password2: this.state.password2,
      })
      .then((response) => {
          console.log(response.data);
          this.props.history.push("/login");
      });
  }

  render(){
      
  }
}