package org.openapijsonschematools.codegen.languages.features;

import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

import org.testng.Assert;
import org.testng.annotations.Test;

// Tests are not final, methods currently just generate documentation as MD tables.
public class DocumentationProviderFeaturesTest {

  @Test(priority = 0)
  void generateDocumentationProviderTable() {
    List<DocumentationProviderFeatures.DocumentationProvider> providers = Arrays.asList(DocumentationProviderFeatures.DocumentationProvider.values());
    StringBuilder sb = new StringBuilder();
    sb.append("### DocumentationProvider\n");
    sb.append("|Cli Option|Description|Property Name|Preferred Annotation Library|Supported Annotation Libraries|\n");
    sb.append("|----------|-----------|-------------|----------------------------|------------------------------|\n");
    providers.forEach(dp -> sb.append(String.format(Locale.ROOT, "|**%s**|%s|`%s`|%s|%s|\n",
        dp.toCliOptValue(),
        dp.getDescription(),
        dp.getPropertyName(),
        dp.getPreferredAnnotationLibrary().toCliOptValue(),
        dp.supportedAnnotationLibraries().stream()
            .map(DocumentationProviderFeatures.AnnotationLibrary::toCliOptValue)
            .collect(Collectors.joining(", "))
    )));
    sb.append("\n");
    Assert.assertTrue(sb.toString().contains("none"));
  }

  @Test(priority = 1)
  void generateAnnotationLibraryTable() {
    List<DocumentationProviderFeatures.AnnotationLibrary> libraries = Arrays.asList(DocumentationProviderFeatures.AnnotationLibrary.values());
    StringBuilder sb = new StringBuilder();
    sb.append("### AnnotationLibrary\n");
    sb.append("|Cli Option|Description|Property Name|\n");
    sb.append("|----------|-----------|-----------|\n");
    libraries.forEach(dp -> sb.append(String.format(Locale.ROOT, "|**%s**|%s|`%s`|\n",
        dp.toCliOptValue(),
        dp.getDescription(),
        dp.getPropertyName()
    )));
    Assert.assertTrue(sb.toString().contains("none"));
    sb.append("\n");
  }
}