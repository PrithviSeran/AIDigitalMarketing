
import Heading from "./Heading"
import Section from "./Section"

const Campaigncontent = ({ campaign }) => {

  return (
    <div className="ml-10 w-[45%] h-[85vh] mt-15">

        <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em] text-center"
            title={campaign.name}
            />
            
        <div className="p-2 w-full bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-t from-black to-purple-500 text-white">
            <span className="flex w-full h-full bg-black text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                <div className="flex flex-col gap-6 py-3 pb-7 text-center">

                    <div className=" w-full py-[0.3em] px-[0.3em] mx-[3em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white mt-9">
                        <span className="flex flex-col w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                        <h5 className="h5 pb-2"> About Yourself </h5>
                        <p>{campaign.user_info}</p>
                        </span>
                    </div>

                    <div className=" w-full py-[0.3em] px-[0.3em] mx-[3em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white">
                        <span className="flex flex-col w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                        <h5 className="h5 pb-2"> Purpose of the Campaign </h5>
                        <p>{campaign.purpose}</p>
                        </span>
                    </div>

                    <div className=" w-full py-[0.3em] px-[0.3em] mx-[3em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white">
                        <span className="flex flex-col w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em]">
                        <h5 className="h5 pb-2"> Your Target </h5>
                        <p>{campaign.target_audience}</p>
                        </span>
                    </div>

                </div>
            </span>
        </div>
    </div>
  )
}

export default Campaigncontent
