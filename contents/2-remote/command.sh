REGION_CODE="nrt"
REPO_NAME=""
docker login $REGION_CODE.ocir.io # REGION_CODEは東京はnrt, 大阪はkix
docker tag custom-wordpress:latest $REGION_CODE.ocir.io/orasejapan/$REPO_NAME/custom-wordpress:latest
docker tag custom-mysql:latest $REGION_CODE.ocir.io/orasejapan/$REPO_NAME/custom-mysql:latest
docker push $REGION_CODE.ocir.io/orasejapan/$REPO_NAME/custom-mysql:latest
docker push $REGION_CODE.ocir.io/orasejapan/$REPO_NAME/custom-mysql:latest