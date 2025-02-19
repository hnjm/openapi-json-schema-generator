<!-- Enter details of the change here. Include additional tests that have been done, reference to the issue for tracking, etc. -->

<!-- Please check the completed items below -->
### PR checklist
 
- [ ] Read the [contribution guidelines](https://github.com/openapi-json-schema-tools/openapi-json-schema-generator/blob/master/CONTRIBUTING.md).
- [ ] Pull Request title clearly describes the work in the pull request and Pull Request description provides details about how to validate the work. Missing information here may result in delayed response from the community.
- [ ] Run the following to [build the project](https://github.com/OpenAPITools/openapi-json-schema-generator#14---build-projects) and update samples:
  ```
  ./mvnw clean package 
  ./bin/generate-samples.sh
  ./bin/utils/export_docs_generators.sh
  ``` 
  Commit all changed files. 
  This is important, as CI jobs will verify _all_ generator outputs of your HEAD commit as it would merge with master. 
  These must match the expectations made by your contribution. 
  You may regenerate an individual generator by passing the relevant config(s) as an argument to the script, for example `./bin/generate-samples.sh bin/configs/python*`. 
  For Windows users, please run the script in [Git BASH](https://gitforwindows.org/).
