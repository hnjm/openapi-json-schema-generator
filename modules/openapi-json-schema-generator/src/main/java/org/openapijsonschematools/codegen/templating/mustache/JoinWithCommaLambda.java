/*
 * Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 * Copyright 2018 SmartBear Software
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.openapijsonschematools.codegen.templating.mustache;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;
import org.openapijsonschematools.codegen.CodegenConfig;

import java.io.IOException;
import java.io.Writer;

/**
 * Split text by 2 spaces and then join the strings with ", "
 *
 * Register:
 * <pre>
 * additionalProperties.put("joinWithComma", new JoinWithCommaLambda());
 * </pre>
 *
 * Use:
 * <pre>
 * {{#joinWithComma}}{{name}}{{/joinWithComma}}
 * </pre>
 */
public class JoinWithCommaLambda implements Mustache.Lambda {
    private CodegenConfig generator = null;

    public JoinWithCommaLambda() {

    }

    public JoinWithCommaLambda generator(final CodegenConfig generator) {
        this.generator = generator;
        return this;
    }

    @Override
    public void execute(Template.Fragment fragment, Writer writer) throws IOException {
        String[] substr = fragment.execute().trim().split("  ");

        writer.write(String.join(", ", substr));
    }
}
