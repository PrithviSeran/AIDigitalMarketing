


const Input = ({
    id,
    placeholder,
    type,
    textArea,
    height,
    customPadding,
    inputRef,
    value = {}
}) => {


    if (textArea == "textarea"){
        return (
            <div className = "text-center pb-3" >
                <textarea value={value.emailContent || ""} ref={inputRef} className = "h-[10em] w-[45em] rounded-[1em] p-7" id={id} type={type} placeholder={placeholder}></textarea>
            </div>
        )  
    }


    return (
        <div className={`
            text-center  
            ${
              customPadding ||"pb-10"
            } `}>
         
            <input ref={inputRef} className = {` ${height || "h-20"} w-[45em] rounded-[1em] p-7`} id={id} type={type} placeholder={placeholder} />
        </div>
    )
}

export default Input;