from fastapi import FastAPI, APIRouter
from app.controller.year_controller import is_leap_year, is_prime
from app.controller.string_controller import split_and_join
from app.dependencies.schema import YearRequest,StringRequest
from app.services.cli_tool import extract_values_from_csv,extract_text_from_pdf
 
app = FastAPI()
router = APIRouter()

csv_path = "C:/Projects/Planck/Phase 1/Resume Extraction/planck-resume-extraction/tests/year-string.csv"
pdf_path = "C:/Projects/Planck/Phase 1/Resume Extraction/planck-resume-extraction/tests/year-string.pdf"

@router.get("/extract-csv/")
async def extract_csv_values():
    
    extracted_year = extract_values_from_csv(csv_path)
    return extracted_year

@router.post("/check-leap-year/")
async def check_leap_year():
    #extracted_year = extract_values_from_csv(csv_path)
    #year= int(extracted_year[0])
    extracted_year = extract_text_from_pdf(pdf_path)
    year = int(extracted_year[0]+extracted_year[1]+extracted_year[2]+extracted_year[3])
    return await is_leap_year(year)

 
# Route for checking prime year
@router.post("/check-prime/")
async def check_prime():
    #extracted_year = extract_values_from_csv(csv_path)
    #year = int(extracted_year[0])  
    extracted_year = extract_text_from_pdf(pdf_path)
    year = int(extracted_year[0]+extracted_year[1]+extracted_year[2]+extracted_year[3])
    return await is_prime(year)
 
# Route for string split and join
@router.post("/string-split-join/")
async def string_split_join():
    extracted_string = extract_values_from_csv(csv_path)
    string = extracted_string[1]
    return await split_and_join(string)

#TODO import a csv file , pdf file and extract values from it and process the router
#docker