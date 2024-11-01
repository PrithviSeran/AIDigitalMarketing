import Heading from "../components/Heading";
import Section from "../components/Section";
import { BackgroundCircles, BottomLine, Gradient } from "../components/design/Hero";
import Input from "../components/Input"
import Button from "../components/Button";
import ButtonGradient from "../assets/svg/ButtonGradient";


const Signup = () => {

    return( 
    <Section id="features">
      <div className="flex flex-row gap-2 container relative z-2">
        <div className="flex flex-wrap gap-5 mb-5 flex-col" style={{
                backgroundImage: `url(./src/assets/benefits/sign-up.svg)`
            }}>
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Create Account"
            />
            <Input
            id = "Name"
            placeholder= "Please enter your Name"
            type="text"
            />
            <Input
            id = "Email"
            placeholder= "Please enter your Email"
            type="text"
            />
            <Input
            id = "Password"
            placeholder= "Please enter your password"
            type="password"
            />
            <Input
            id = "Password Again"
            placeholder= "Please enter your password again"
            type="password"
            />
            <div className="text-center p-5">
                <Button className="w-[30em] text-center">
                    Create Account
                </Button>
            </div>

        </div>

        <div>
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Already have an account? Sign-in."
            />

            <div className="text-center mb-[3em]">
                <Button className="w-[30em] text-center">
                    Sign-in
                </Button>
            </div>
        </div>
        
      </div>
      <BackgroundCircles />
      <ButtonGradient />
    </Section>
    );
}

export default Signup;