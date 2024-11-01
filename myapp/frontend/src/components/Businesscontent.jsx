
import Heading from "./Heading"
import Section from "./Section"
import ButtonGradient from "../assets/svg/ButtonGradient";
import Input from "./Input";


const Businesscontent = ({ business }) => {
  return (
    <div className="w-[45%] h-[85vh]">

        <Heading
            className="md:max-w-md lg:max-w-2xl text-center"
            title={business.name}
            />
        <div className="p-2 w-full bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-t from-black to-purple-500 text-white">
            <span className="flex w-full h-full bg-black text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                <div className="flex flex-col gap-6 py-3 pb-7">

                    <div className=" py-[0.3em] px-[0.3em] mx-[3em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white mt-9">
                        <span className="flex flex-col w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                        <h5 className="h5 pb-2"> Content </h5>
                        <p>{business.content}</p>
                        </span>
                    </div>

                    <div className="py-[0.3em] px-[0.3em] mx-[3em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white">
                        <span className="flex flex-col w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                        <h5 className="h5 pb-2"> Please Enter this Organization's Email: </h5>
                        <Input/>
                        </span>
                    </div>
                </div>
            </span>
        </div>
    </div>
  )
}

export default Businesscontent
