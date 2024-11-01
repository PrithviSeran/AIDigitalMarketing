import Heading from "./Heading"
import Button from "./Button"
import Input from "./Input"
import ButtonGradient from "../assets/svg/ButtonGradient";


const Emailtemplate = (emailContent) => {
  return (
    <div className="w-[55%] h-[85vh]">

        <Heading
        title="Auto Generated Email"
        />

        <div className="flex flex-col justify-center align-center">
            <Input
            textArea = "textarea"
            value = {emailContent}
            />
            
            <div className="text-center">
                <Button
                className="w-[17em]">
                    Send Email
                </Button>
            </div>
        </div>

        <ButtonGradient/>

    </div>
  )
}

export default Emailtemplate
